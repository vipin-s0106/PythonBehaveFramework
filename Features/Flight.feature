Feature: Testing of Flight Application

    Background:
      #noinspection CucumberUndefinedStep
      Given I navigated to the "FlightApplication_URL" page
      And I wait for "2" second


    Scenario: To check user can find a flight from Paris to London
      And I verified the "FlightApplication_URL" page is opened
      When I click on departure city dropdown
      And I click on "dropdown option" with "text" "Boston"
      And I click on destination city dropdown
      And I click on "dropdown option" with "text" "Dublin"
      And I click on "button" with "text" "Find Flights"
      Then I verified "object" with "text" "Flights from Boston to Dublin:" present
      And I take the screenshot with filename "image"