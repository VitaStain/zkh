from drf_spectacular.utils import OpenApiParameter


def auto_docstring():
    def dec(instance):
        if instance.__doc__:
            instance.__doc__ += """\n\n"""
        else:
            instance.__doc__ = """"""

        if instance.__dict__.get("ordering"):
            instance.__doc__ += "```сортировка по умолчанию```: \n\n * "
            instance.__doc__ += "\n * ".join(instance.ordering)
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("ordering_fields"):
            instance.__doc__ += (
                "```Ordering``` сортировка по следующим категориям: \n\n * "
            )
            instance.__doc__ += "\n * ".join(instance.ordering_fields)
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("search_models"):
            instance.__doc__ += (
                "```Search``` поиск по следующим связаным моделям: \n\n * "
            )
            instance.__doc__ += "\n * ".join(
                [search_model.__name__ for search_model in instance.search_models]
            )
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("search_fields"):
            instance.__doc__ += "```Search``` поиск по следующим полям: \n\n * "
            instance.__doc__ += "\n * ".join(instance.search_fields)
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("filterset_fields"):
            instance.__doc__ += "```Filter``` фильтрация по следующим полям: \n\n * "
            instance.__doc__ += "\n * ".join(instance.filterset_fields)
            instance.__doc__ += "\n\n"

        return instance

    return dec


