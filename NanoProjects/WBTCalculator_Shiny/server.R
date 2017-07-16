#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
#comments removed here
shinyServer(function(input, output) {
  
 
  output$cel <- renderText({ 
    paste(round((input$temp * atan(0.151977*(input$rh+8.313659)^0.5)+
             atan (input$temp + input$rh) - atan (input$rh - 1.676331) + 
             0.00391838 * input$rh^(3/2) * atan (0.023101*input$rh) -
             4.686035),2)," C")
    
  })
  
  output$Fah <- renderText({ 
    paste(round((round((input$temp * atan(0.151977*(input$rh+8.313659)^0.5)+
                   atan (input$temp + input$rh) - atan (input$rh - 1.676331) + 
                   0.00391838 * input$rh^(3/2) * atan (0.023101*input$rh) -
                   4.686035),2)*1.8+32),2)," F") 
  }) 
  
  
})