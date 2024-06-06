from bedjango.dto import DTO
from django.db import models
from rest_framework import serializers
from django.core.paginator import Paginator


class GeneralRepository:

    _paginator: Paginator

    def __init__(self) -> None:
        self._paginator = Paginator

    def get_paginator(self, **args) -> Paginator:
        return self._paginator(**args)

    def paginate_if_has_request_page_and_page_size(
        self,
        query_params: DTO,
        filtered_queryset: models.Model,
        serializer: serializers.Serializer,
    ):
        if query_params._raw_request.query_params.get("page_size") == None:
            return {
                "total": len(filtered_queryset.values()),
                "data": filtered_queryset.values(),
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
                "total": paginator.count,
                "total_pages": paginator.num_pages,  # Added total pages
                "next": page.next_page_number() if page.has_next() else None,
                "previous": (
                    page.previous_page_number() if page.has_previous() else None
                ),
                "data": serializer.data,
            }
