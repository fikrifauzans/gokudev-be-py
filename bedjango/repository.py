from bedjango.dto import DTO
from django.db import models
from rest_framework import serializers
from django.core.paginator import Paginator
from django.utils import timezone


class GeneralRepository:

    _paginator: Paginator
    _model: models.Model
    _serializer: serializers.Serializer

    def __init__(self) -> None:
        self._paginator = Paginator

    def get_paginator(self, **args) -> Paginator:
        return self._paginator(**args)

    def create(self, data: dict) -> any:
        instance = self.model.objects.create(**data)
        return self.serializer(instance).data

    def get_by_id(self, id: int) -> any:
        instance = self.model.objects.filter(id=id, deleted_at__isnull=True).first()
        if instance:
            return self.serializer(instance).data
        return None

    def update(self, id: int, data: dict) -> any:
        instance = self.model.objects.filter(id=id, deleted_at__isnull=True).first()
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()
            return self.serializer(instance).data
        return None

    def get(self, query_params: DTO) -> any:
        filtered_queryset = self.model.objects.filter(**query_params._query_set)
        return self.paginate_if_has_request_page_and_page_size(
            query_params, filtered_queryset, self.serializer
        )

    def delete(self, id: int) -> any:
        instance = self.model.objects.filter(id=id, deleted_at__isnull=True).first()
        if instance:
            instance.deleted_at = timezone.now()
            instance.save()
            return {"message": "Deleted successfully"}
        return {"message": "Instance not found"}

    def paginate_if_has_request_page_and_page_size(
        self,
        query_params: DTO,
        filtered_queryset: models.Model,
        serializer: serializers.Serializer,
    ):
        order_by = query_params._raw_request.query_params.get("order_by", "id")
        order_direction = query_params._raw_request.query_params.get(
            "order_direction", "asc"
        )
        if order_direction == "desc":
            order_by = f"-{order_by}"

        filtered_queryset = filtered_queryset.order_by(order_by)

        if query_params._raw_request.query_params.get("page_size") == None:
            return {
                "data": filtered_queryset.values(),
                "meta": {
                    "total": len(filtered_queryset.values()),
                },
            }
        else:
            paginator = self._paginator(
                filtered_queryset,
                query_params._raw_request.query_params.get("page_size", 10),
            )
            page = paginator.get_page(
                query_params._raw_request.query_params.get("page", 1)
            )

            serializer = serializer(page.object_list, many=True)
            return {
                "data": serializer.data,
                "meta": {
                    "total": paginator.count,
                    "total_pages": paginator.num_pages,  # Added total pages
                    "next": page.next_page_number() if page.has_next() else None,
                    "previous": (
                        page.previous_page_number() if page.has_previous() else None
                    ),
                },
            }
