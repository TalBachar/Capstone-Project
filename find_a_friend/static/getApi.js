//.js  fetch images/name from petfinder APi

// prepare Data key+secret
//"use strict";

var pet;
var breed;
var age = 0;
var page = 0;
var total_count;

$(function () {
  console.log(token);
  loadData();
});
//load data
function loadData() {
  $("form").submit((event) => {
    event.preventDefault();
    pet = $("#pet").val();
    breed = $("#breed").val();
    age = $("#age").val();
    page = 1;
    fetchAnimals(pet, breed, "10020", age, page);
  });
}
//fetch
function fetchAnimals(pet, breed, location, age, page) {
  console.log(token);
  fetch(
    `https://api.petfinder.com/v2/animals?type=${pet}&breed=${breed}&age=${age}&location=${location}&status=adoptable&distance=25&page=${page}&limit=6&sort=recent`, // add ${page}
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
  ('<p class="text-center">${getResponse.animals.page}</p>');
  console.log("Total Results:", getResponse.pagination.total_count);
  total_count = getResponse.pagination.total_count;

  for (let i = 0; i < getResponse.animals.length; i++) {
    console.log("Size of array: ", getResponse.animals[i].photos.length);
    if (getResponse.animals[i].photos.length > 0) {
      $("#printApi ").append(`

      <div class="col-sm-4">
        <div class="card" style="width: 300px;">
        <a href="${getResponse.animals[i].url}">
          <div class="card "  style="height: 400x;">
            <img class="card-img-top" style="height: 300px;" src="${getResponse.animals[i].photos[0].medium}">
          </div>
          </a>
          <div class="card-body">
            <h3 class="card text-center text-danger font-weight-bold ">${getResponse.animals[i].name}</h3>
            <p class="text-center">${getResponse.animals[i].breeds.primary}</p>
            <p class="text-center">${getResponse.animals[i].gender}</p>
            <p class="text-center">${getResponse.animals[i].age}</p>

			<form method="post" action="/pets/create" enctype="multipart/form-data">
			<center>
			<input type="hidden" name="fav_name" style="text-align:center;" value = "${getResponse.animals[i].name}" />
			<input type="hidden" name="fav_age" style="text-align:center;" value = "${getResponse.animals[i].age}" />
			<input type="hidden" name="fav_breed" style="text-align:center;" value = "${getResponse.animals[i].breeds.primary}" />
			<input type="hidden" name="fav_url" style="text-align:center;" value = "${getResponse.animals[i].url}" />
			<input type="hidden" name="fav_image" style="text-align:center;" value = "${getResponse.animals[i].photos[0].medium}" />
			<input class="btn btn-primary" type="submit" value="Add Favorites" />
			</form>
			</center>

          </div>
        </div>
      </div>
     `);
    } else {
      $("#printApi ").append(`

      <div class="col-sm-4">
        <div class="card" style="width: 300px;">
        <a href="${getResponse.animals[i].url}">
          <div class="card "  style="height: 400x;">
            <img class="card-img-top" style="height: 300px;" src="https://g.petango.com/shared/Photo-Not-Available-dog.gif">
          </div>
          </a>
          <div class="card-body">
            <h3 class="card text-center text-danger font-weight-bold ">${getResponse.animals[i].name}</h3>
            <p class="text-center">${getResponse.animals[i].breeds.primary}</p>
            <p class="text-center">${getResponse.animals[i].gender}</p>
            <p class="text-center">${getResponse.animals[i].age}</p>
			<form method="post" action="/pets/create" enctype="multipart/form-data">
			<center>

			<input type="hidden" name="fav_name" style="text-align:center;" value = "${getResponse.animals[i].name}" />
			<input type="hidden" name="fav_age" style="text-align:center;" value = "${getResponse.animals[i].age}" />
			<input type="hidden" name="fav_breed" style="text-align:center;" value = "${getResponse.animals[i].breeds.primary}" />
			<input type="hidden" name="fav_url" style="text-align:center;" value = "${getResponse.animals[i].url}" />
			<input type="hidden" name="fav_image" style="text-align:center;" value = "${getResponse.animals[i].photos[0].medium}" />
			<input class="btn btn-primary" type="submit" value="Add Favorites" />
			</form>
			</center>
          </div>
        </div>
      </div>
     `);
    }
  }
}

$("#loadMore").on("click", function () {
  event.preventDefault();
  page++;
  console.log("Page is ", page);
  fetchAnimals(pet, breed, "10020", age, page);
});

$("#loadLess").on("click", function () {
  event.preventDefault();
  page--;
  console.log("Page is ", page);
  fetchAnimals(pet, breed, "10020", age, page);
});

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
