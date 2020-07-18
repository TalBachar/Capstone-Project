//.js  fetch images/name from petfinder APi

// prepare Data key+secret
'use strict';


$(function () {
  console.log(token);
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
  fetch(`https://api.petfinder.com/v2/animals?type=${pet}&breed=${breed}&location=${location}&distance=25&limit=25`, {
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
  $('#printApi').html('');
  for(let i=0; i<getResponse.animals.length; i++) {
     $('#printApi ').append(`

  <div class="col-sm-4">
      <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="${getResponse.animals[i].photos[0].medium}" >
        <div class="card-body">
          <h5 class="card text-center ">${getResponse.animals[i].name}</h5>
          <p class="text-center">${getResponse.animals[i].breeds.primary}</p>
          <p class="text-center">${getResponse.animals[i].gender}</p>
          <p class="text-center"> Contact: ${getResponse.animals[i].contact.phone}</p>
          <h5 class="card text-center bg-danger mb-3"><a href="${getResponse.animals[i].url}" >More About!</a></h5>
        </div>
      </div>
</div>

      `);

 }
}
//error handling
function errorHandling(response) {
  console.log(response);
  if(!response.animals) {
    coutError("Error!");
    return
  }
  if(response.animals.length == 0) {
    coutError("nothing to show!");
    return
  }
  return
}

function coutError(message) {
  $('#printApi ul').html('');
  $('#printApi ul').append(`<li>${message}</li>`);
  console.log(message);
}
