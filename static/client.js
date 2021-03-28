function findrecipes() {
    var dietp = document.getElementById('dietp');
    var timep = document.getElementById('time');
    var calories = document.getElementById('calories');
    var course = document.getElementById('course');

    var diet_preference = dietp.options[dietp.selectedIndex].text;
    var time_required = timep.options[timep.selectedIndex].value;
    var caloric_preference = calories.options[calories.selectedIndex].value;
    var course_preference = course.options[course.selectedIndex].text;
    var ingredients = ['olive oil','chicken','butter'];

    var xhr = new XMLHttpRequest();
    var loc = window.location;
    xhr.open('POST', `${loc.protocol}//${loc.hostname}:${loc.port}/findrecipe`,
        true);
    xhr.onerror = function () {
        alert(xhr.responseText);
    };
    xhr.onload = function (e) {
        
    };

    var fileData = new FormData();
    fileData.append("dietp", diet_preference);
    fileData.append("time", time_required);
    fileData.append("calories", caloric_preference);
    fileData.append("course", course_preference);
    fileData.append("ingredients", ingredients);
    xhr.send(fileData);
}
