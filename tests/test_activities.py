def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activity_name in payload
    assert len(payload) == 9


def test_get_activities_returns_expected_activity_fields(client):
    # Arrange
    expected_activity = "Programming Class"

    # Act
    response = client.get("/activities")

    # Assert
    activity = response.json()[expected_activity]
    assert activity["description"] == "Learn programming fundamentals and build software projects"
    assert activity["schedule"] == "Tuesdays and Thursdays, 3:30 PM - 4:30 PM"
    assert activity["max_participants"] == 20
    assert activity["participants"] == ["emma@mergington.edu", "sophia@mergington.edu"]