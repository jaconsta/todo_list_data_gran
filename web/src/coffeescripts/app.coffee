$ = require 'jquery' # For Node.js compatibility

#http://www.webdesignerdepot.com/2013/05/a-taste-of-coffeescript-part-2/

$(document).ready ->
  # Validate if the user is logged in
  if localStorage.getItem 'access_token'
    $('body').append localStorage.getItem 'access_token'

  
  


$('#register_submit').on "click", (e) -> 
  e.preventDefault()

  user_data = 
    email: $('#register_email').val()
    password: $('#register_password').val()

  $.ajax "http://localhost:8080/user",
    type: 'POST'
    contentType: "application/json"
    data: JSON.stringify(user_data)
    error:(jqXHR, textStatus, errorThrown) ->
      $('body').append "Error creating user."
    success: (data, textStatus, jqXHR) ->
      $('body').append "Successful AJAX call: #{data}"

$('#login_submit').on "click", (e) -> 
  e.preventDefault()

  user_data = 
    email: $('#login_email').val()
    password: $('#login_password').val()

  $.ajax "http://localhost:8080/login",
    type: 'POST'
    contentType: "application/json"
    data: JSON.stringify(user_data)
    error:(jqXHR, textStatus, errorThrown) ->
      $('body').append "Error creating user."
    success: (data, textStatus, jqXHR) ->
      $('body').append "Successful AJAX call: #{data}"
      console.log(data)
      
      localStorage.setItem 'access_token', data.token