# 查看当前路径
getwd()
# 设置工作路径
setwd("d:/Gitwork/usermaster/R")

# dash
install.packages("shinydashboard")

# 仪表盘UI
library(shinydashboard)
library(shiny)

dashboardPage(
  #标题
  dashboardHeader(), 
  #侧栏
  dashboardSidebar(), 
  #主体
  dashboardbody()
)

# app.R 空白仪表盘搭建

ui <- dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody()
)

sever <- function(input,output){ }

shinyApp(ui,sever)

# app.R

ui <- dashboardPage(
  dashboardHeader(title = "Basic dashboard"),
  dashboardSidebar(),
  dashboardBody(
    # boxes need to be in put in a row (or column)
    fluidRow(
      box(plotOutput("Plot1",height = 250)),
      
      box(
        title = "Controls",
        sliderInput("slider","Number of observations:",1,100,50)
      )
    )
  )
)

sever <- function(input,output) {
  set.seed(122)
  histdata <- rnorm(500)
  
  output$plot1 <- renderPlot({
    data <- histdata[seq_len(input$slider)]
    histdata
  })
}

shinyApp(ui,sever)









































