$(function() {
  var key = localStorage.getItem('token_key')
  $("#userInfo").html("<strong>Hiiii</strong>");
  console.log(key)
  $("#userRegister").html("<p>Not You! <button type=\"button\" class=\"btn btn-primary\">Register</button></p>");
  localStorage.setItem('token_key', 'helllo')
});