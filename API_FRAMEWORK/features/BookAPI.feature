Feature: Verify if Books are added and deleted using Library API

  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to the Library
    When we execute the AddBook Post API method
    Then book is successfully added
    