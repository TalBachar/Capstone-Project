//.js  fetch images/name from petfinder APi

// prepare Data key+secret
"use strict";

$(function () {
  console.log(token);
  loadData();
});
//load data
function loadData() {
  $("form").submit((event) => {
    event.preventDefault();
    const pet = $("#pet").val();
    const breed = $("#breed").val();
    const age = $("#age").val();
    const page = $("#page").val(); // track page --> not implemented yet
    fetchAnimals(pet, breed, "10020", age);
  });
}
//fetch
function fetchAnimals(pet, breed, location, age, page) {
  console.log(token);
  fetch(
    `https://api.petfinder.com/v2/animals?type=${pet}&breed=${breed}&location=${location}&age=${age}&distance=25&page=3`, // add ${page}
    {
      headers: {
        Authorization: `Bearer ${token.access_token}`,
      },
    }
  )
    .then((getData) => getData.json())
    .then((getResponse) => decodeData(getResponse))
    .catch((error) => coutError(error.message));
}

//retrieved the API data as JSON and into the html//
function decodeData(getResponse) {
  errorHandling(getResponse);
  $("#printApi").html("");
  for (let i = 0; i < getResponse.animals.length; i++) {
    $("#printApi ").append(`

  <div class="col-sm-4">
      <div class="card" style="width: 300px;">
      <a href="${getResponse.animals[i].url}">
        <img class="card-img-top" src="${getResponse.animals[i].photos[0].medium}">
      </a>
        <div class="card-body">
          <h3 class="card text-center text-danger font-weight-bold ">${getResponse.animals[i].name}</h3>
          <p class="text-center">${getResponse.animals[i].breeds.primary}</p>
          <p class="text-center">${getResponse.animals[i].gender}</p>
          <p class="text-center">${getResponse.animals[i].age}</p>
          <form action="${getResponse.animals[i].url}" class="text-center">
              <input type="submit" class="btn btn-danger" value="More info about ${getResponse.animals[i].name}" />
          </form>
        </div>
      </div>
</div>


      `);
  }
}

//error handling
function errorHandling(response) {
  console.log(response);
  if (!response.animals) {
    coutError("Error!");
    return;
  }
  if (response.animals.length == 0) {
    coutError("Nothing to show!");
    return;
  }
  return;
}

function coutError(message) {
  $("#printApi ul").html("");
  $("#printApi ul").append(`<li>${message}</li>`);
  console.log(message);
}
