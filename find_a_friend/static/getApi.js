//.js  fetch images/name from petfinder APi

// prepare Data key+secret
'use strict';


$(function () {
  console.log('Top Result!');
  loadData();
})
//load data
function loadData() {
  $('form').submit(event => {
    event.preventDefault();
    const pet = $('#pet').val();
    const breed = $('#breed').val();
    fetchAnimals(pet, breed, 'NY');
  });
}
//fetch
function fetchAnimals(pet,breed,location) {
  console.log(token);
  fetch(`https://api.petfinder.com/v2/animals?type=${pet}&breed=${breed}&location=${location}&status=adoptable&distance=25`, {
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
    for(let j=0; j<1; j++) {
     $('#printApi ul').append(`<li>
      <br>
      <br>
     <h1>${getResponse.animals[i].name}</h1>
     <img src="${getResponse.animals[i].photos[j].small}" >
     <h5><p>${getResponse.animals[i].breeds.primary} </p>
     <p>${getResponse.animals[i].age} </p>
     <p>${getResponse.animals[i].size}</p>
     <p>${getResponse.animals[i].description}</p>
     <a href="${getResponse.animals[i].url}" >Contact!</a>
     </h5>

     </li>`);
   }
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
