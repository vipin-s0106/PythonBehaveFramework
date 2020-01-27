Feature: Testing of Flight Application

  Background: 
    Given I navigated to the "FlightApplication_URL" page
    And I wait for "5" second


  @scenario1
  Scenario Outline: To check user can find a flight scenario1
    And I am running "123456" testcase
    And I verified the "FlightApplication_URL" page is opened
    When I click on departure city dropdown
    And I click on "dropdown option" with "text" "<Departure_City>"
    And I click on destination city dropdown
    And I click on "dropdown option" with "text" "<Destination_City>"
    And I click on "Find Fights" with "class" "btn btn-primary"
    And I wait for "5" second
    Then I verified "object" with "text" "Flights from <Departure_City> to <Destination_City>: " present
    And I take the screenshot with filename "image.png"


  Examples:
    | Departure_City | Destination_City |
    | Boston         | Dublin           |
    | Paris          | Rome             |



  @scenario2
  Scenario Outline: To check user can find a flight scenario1
    And I am running "123456" testcase
    And I verified the "FlightApplication_URL" page is opened
    When I click on departure city dropdown
    And I click on "dropdown option" with "text" "<Departure_City>"
    And I click on destination city dropdown
    And I click on "dropdown option" with "text" "<Destination_City>"
    And I click on "Find Fights" with "class" "btn btn-primary"
    And I wait for "5" second
    Then I verified "object" with "text" "Flights from <Departure_City> to <Destination_City>: " present
    And I take the screenshot with filename "image.png"


  Examples:
    | Departure_City | Destination_City |
    | Portland       | Cairo            |





  #C:\Users\vipin\PycharmProjects\PythonBehaveFramework\Lib\allure-2.7.0\bin\allure serve result