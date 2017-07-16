#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
#Comments removed here
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Calculate WBT"),
  # Subtitle
  h5("Calculate Wet Bulb Temperature from Ambient Temrerature"),
  h6("Author: A K Pradhan"),
  hr(),
  
  sidebarLayout(
    sidebarPanel(
      #Help and documentation
      h4('Documentation and Help'),
      h5("For sake of simplicity, the Temperature values to convert are limited in range from 0 to 60 C","\n"," and Relative Humidity ranging from 0-100%"),
      h5("When slider (input) is moved, the value converted will be calculated on server. The original and equivalent values will be displayed on right side of the screen (reactive controls) "),
      br(),
     
       h4('Step 1:'),
      br(),
      # Input 2. A slider to select a temperature to convert. Limited in range from -32 to 300
      # Initial value is 32 F, equivalent to 0 C
      sliderInput("temp",
                  "Select Ambient Temperature :",
                  min = 0,
                  max = 150,
                  value = 32),
      sliderInput("rh",
                  "Select a RH :",
                  min = 0,
                  max = 100,
                  value = 65)
    ),
    
    # Show the original and converted value as a reactive operation. Each time an input is updated, those values are
    # Calculated on the server and returned here
    mainPanel(
      h2(textOutput("sourcetemp")),
      h2("The Wet Bulb Temperature is "),
      h2(textOutput("cel")),
      h2(textOutput("Fah"))
    )
    
  )
))
