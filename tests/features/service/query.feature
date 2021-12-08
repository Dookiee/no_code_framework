Feature: Query Test in different search engines

  @test
  Scenario Outline: Zippopotam country query api
    When Create Get Request in zippopotam_service country_query API: <query_param_url> as query param: <query_string> as query string
    Then the response contains results for <status_code>
    And I validate the response against <validation_json>

    Examples:
    | query_param_url  | status_code | validation_json                                                                                                              | query_string    |
    |          {}      |    200      | {"post code": "90210", "country": "United States", "places/0/state": "California",  "places/0/place name": "Beverly Hills" } |  us/90210       |
    |          {}      |    200      | {"post code": "110001", "country": "India", "places/0/state": "New Delhi", "places/0/place name": "Janpath" }                |  in/110001      |
    |          {}      |    404      | {}                                                                                                                           |  acc/110001     |
    |          {}      |    404      | {}                                                                                                                           |  us/110001      |
    |          {}      |    200      | {"post code": "90210", "country": "US"}                                                                                      |  us/90210       |
    |          {}      |    404      | {}                                                                                                                           |  us/90210       |
    |          {}      |    404      | {"post code/places/state": "California"}                                                                                     |  us/90210       |

  @duckduckgo
  Scenario Outline: Duck duck go search engine query api
    When Create Get Request in duck_duck_go_service custom_query API: <query_param_url> as query param: <query_string> as query string
    Then the response contains results for <status_code>
    And I validate the response against <validation_json>

    Examples:
    | query_param_url  | status_code | validation_json                    | query_string |
    | q={}&format=json |    200      | {"meta/name": "Just Another Test"} |  hello       |
    | q={}&format=json |    200      | {"meta/name": "Just Test"}         |  hello       |

  @google
  Scenario Outline: Google search engine query api
    When Create Get Request in google_service custom_query API: <query_param_url> as query param: <query_string> as query string
    Then the response contains results for <status_code>
    And I validate the response against <validation_json>

    Examples:
    | query_param_url  | status_code | validation_json | query_string |
    | q={}&format=json |    200      | {}              |  hello       |


