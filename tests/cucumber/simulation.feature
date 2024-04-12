When CLI app is executed
Then I should be prompted to enter simulation settings

Given CLI app is executed
When I successfully enter in simulation settings
Then I should see a plot appear on the screen.

Given I set grid size to 1x3
And I set obstacles to 0
And I add a Fox to 0,0
And I add a Rabbit to 0,1
When I step
Then Rabbit should be in 0,2
And Fox should be in 0,1

Given I set grid size to 2x2
And I add 4 Fox
And I add 8 Rabbit
When a Rabbit dies
Then Fox population should be 3
And Rabbit population should be 7
