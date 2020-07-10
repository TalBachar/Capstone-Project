var apikey="VjH9YrMKFfA5RZa54XZB3PLY2IpNTbQtuQmbzIP7ax9JF0uYMx";
var apisecret="VPUV6SU4l8lSyxn6ZjcwJqS8ZpZfoRxVapAtt2ja";
let token=""

function Token() {
    fetch('https://api.petfinder.com/v2/oauth2/token', {
        method: "POST",
        body: "grant_type=client_credentials&client_id=" + apikey + "&client_secret=" + apisecret,
        headers: {
           "Content-Type": "application/x-www-form-urlencoded"
         }
      })

    .then(function(response) {
      return response.json();
    })

    .then(function(data) {
      token= data
      console.log('token', data)
    })
}
Token();
