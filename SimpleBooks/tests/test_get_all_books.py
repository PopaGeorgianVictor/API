from SimpleBooks.request_folder.get_all_books import get_all_books


class TestGetBooks:
    def test_get_all_books_no_filter_check_response_status(self):
        response = get_all_books()
        assert response.status_code, f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"

    def test_get_all_books_no_filter_check_number_of_results(self):
        response = get_all_books()
        assert len(response.json()) == 6, f"Error: invalid number of books returned.Expected: 6, actual: {len(response)}"

    def test_get_all_books_filter_by_type_fiction(self):
        response = get_all_books("fiction").json()
        assert len(response) == 4, f"Expected: 4, Actual: {len(response)}"
        for i in range(len(response)):
            assert response[i]["type"] == "fiction", f"Error: Book {response[i]['name']} has an invalid type"

    def test_get_all_books_filter_by_type_non_fiction(self):
        response = get_all_books("non-fiction").json()
        assert len(response) == 2, f"Expected: 2, Actual: {len(response)}"
        for i in range(len(response)):
            assert response[i]["type"] == "non-fiction", f"Error: Book {response[i]['name']} has an invalid type"

    def test_get_all_books_filter_by_invalid_type(self):
        response = get_all_books("£@$%^")
        assert response.status_code == 400
        assert response.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", "Error is not correct"

    def test_get_all_books_filter_by_superior_invalid_limit(self):
        response = get_all_books(limit=25)
        assert response.status_code == 400
        assert response.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."

    def test_get_all_books_filter_by_type_fiction_and_valid_limit(self):
        response = get_all_books("fiction",3).json()
        for i in range(len(response)):
            assert response[i]["type"] == "fiction", f"Error: fiter by type fiction did not work "

        assert len(response) == 3, f"Expected: 3, Actual: {len(response)}"