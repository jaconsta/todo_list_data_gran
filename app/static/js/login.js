$(function() {
  var key = localStorage.getItem('jwtToken')
  // The user is authenticated
  console.log('key', key)
  if (key != null)
    window.location.href ='/users/'
});


$('#loginForm').submit(function (event) {
    event.preventDefault();

    var login_url = 'http://localhost:8080/api/v1/login'
    var form = {
      email: $( "#inputEmail" ).val(),
      password: $( "#inputPassword" ).val()
    };
    console.log('form', JSON.stringify(form));
    $.ajax({
      url: login_url,
      method: 'POST',
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify(form),
      success: function(res) {
        console.log('it worked!!', res);
        if (res.token != null){
        localStorage.setItem('jwtToken', res.token)
        } else {
        console.log('response with no token')
        }
      },
      error: function(err) {
        console.log('Ohh no an error!!');
        console.log(err.responseText);
      }
    });
});