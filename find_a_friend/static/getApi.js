//.js  fetch images/name from petfinder APi

// prepare Data key+secret

$(function () {
  console.log('Top Result!');
  loadData();
})
//load data
function loadData() {
  $('form').submit(event => {
    event.preventDefault();
    const text_search = $('#text_search').val();
    const type = $('input[name="typeOfAnimal_rg"]:checked').val();
    fetchAnimals(type, 'New York', text_search);
    console.log(text_search);

  });
}
//fetch
function fetchAnimals(type, zip, text_search) {
  fetch(`https://api.petfinder.com/v2/animals?type=${type}&location=${zip}&status=adoptable&distance=25`, {
    headers: {
      Authorization: `Bearer ${token.access_token}`
    }
  })
    .then(getData => getData.json())
    .then(getResponse => decodeData(getResponse))
    .catch(error => coutError(error.message));
}

  //retrieved the API data as JSON and into the html//
function decodeData(getResponse) {
  errorHandling(getResponse);
  $('#printApi ul').html('');
  for(let i=0; i<getResponse.animals.length; i++) {
     $('#printApi ul').append(`<li>
     <h1>${getResponse.animals[i].name}</h1> <h4>${getResponse.animals[i].breeds.primary} - ${getResponse.animals[i].age}</h4>
     <p><img src="${getResponse.animals[i].photos[0].small}">
     ${getResponse.animals[i].description}</p>

     <a href="${getResponse.animals[i].url}" >More details</a>

     </li><br>`);

  }

}
//error handling
function errorHandling(getResponse) {
  console.log(getResponse);
  if(!getResponse.animals) {
    coutError("Error!");
    return
  }
  if(getResponse.animals.length == 0) {
    coutError("nothing to show!");
    return
  }
}

function coutError(message) {
  $('#printApi ul').html('');
  $('#printApi ul').append(`<li>${message}</li>`);
  console.log(message);
}
