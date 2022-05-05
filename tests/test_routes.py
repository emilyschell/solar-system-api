def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "New York",
        "description": "ny 4evr",
        "moons": 2
    }


def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "New York",
        "description": "ny 4evr",
        "moons": 2
    },
        {
        "id": 2,
        "name": "Rocky McPlanet",
        "description": "i luv 2 climb rocks",
        "moons": 0
    }]


def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "The Best!",
        "moons": 5
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet has been successfully created!"
