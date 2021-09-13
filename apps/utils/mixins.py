class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        try:
            return self.serializer_actions[self.action]  # type: ignore
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()  # type: ignore
