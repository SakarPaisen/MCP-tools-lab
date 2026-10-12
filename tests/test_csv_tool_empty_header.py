from mcp_tools_lab.tools.csv_tool import inspect_csv


def test_empty_header_indices_reports_positions():
    result = inspect_csv("name,,age\nAda,20,x\nBob,30,y")
    assert result["empty_header_indices"] == [1]


def test_whitespace_only_header_reports_position():
    result = inspect_csv("name, ,age\nAda,20,x")
    assert result["empty_header_indices"] == [1]


def test_empty_header_indices_lists_every_blank_column():
    result = inspect_csv("a,,c,,e\n1,2,3,4,5")
    assert result["empty_header_indices"] == [1, 3]


def test_header_names_are_still_columns():
    result = inspect_csv("name,,age\nAda,20,x")
    assert result["columns"] == ["name", "", "age"]


def test_empty_input_has_no_empty_header_indices():
    assert inspect_csv("")["empty_header_indices"] == []


def test_blank_header_is_still_valid():
    assert inspect_csv("name,,age\nAda,20,x")["valid"] is True


def test_malformed_csv_does_not_report_empty_header_indices():
    # A document that will not parse has no header positions to name.
    result = inspect_csv('name\n"unfinished')
    assert result["valid"] is False
    assert "empty_header_indices" not in result
