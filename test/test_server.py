from testyoke.server import get_parser


class TestServer:
    def test_get_parser_junit(self):
        content_type = 'application/xml+junit'
        parser = get_parser(content_type)

        assert callable(parser.parse)

    def test_get_parser_default(self):
        content_type = None
        parser = get_parser(content_type)

        assert callable(parser.parse)

