let drag_cols = document.getElementsByClassName("place_to_drag");
for (let elem of drag_cols) {
    elem.addEventListener('dragover', function() {drag_move(event)})//для всех мест куда перемещается элемент делаем обработку перемещающегося элемента
}

let drag_elements = document.getElementsByClassName("drag_element");
for (let elem of drag_elements) {
    elem.draggable = true;
    elem.addEventListener("dragstart", function() {drag_start(event)} );//отслежвание нажатия и начала движения
    elem.addEventListener('dragend', function() {drag_end(event)});//отслежвание отпускания и окончания движения
}

function drag_start(event){
    if (event.target.className.indexOf("drag_element") != -1){event.target.classList.add('selected');}
};
function drag_move(event) {
    event.preventDefault();
    const activeElement = document.querySelector('.selected');
    let currentElement = event.target;
	while (currentElement != null && currentElement.className.indexOf("place_to_drag") == -1) {
	    currentElement = currentElement.parentElement;
	};
	currentElement.appendChild(activeElement);
};


function drag_end(event){
    let currentElement = event.target;
	while (currentElement != null && currentElement.className.indexOf("place_to_drag") == -1) {
	    currentElement = currentElement.parentElement;
	};
	console.log(currentElement);
    change_value(event, event.target.id, -currentElement.id);
    event.target.classList.remove('selected');
};
function change_value(event, id, column_id){
    const data = JSON.stringify({'id':id, 'column_id':column_id});

    const request = new XMLHttpRequest();
    request.open("post", "/api/v1/action/"+id+"/"+column_id);
    request.setRequestHeader("Content-Type", "application/json");

    request.onload = () => {
        if (request.status == 200) {
            const user = JSON.parse(request.responseText)
            console.log(user);
        } else {
            console.log("Server response: ", request.statusText);
        }
    };
    request.send(data);
};














function add_column(project_id){
    console.log(project_id);
    const text = document.getElementById('add_column');
    const data = JSON.stringify({});
    const request = new XMLHttpRequest();
    request.open("post", "/api/v1/column/"+project_id+'/'+text.value);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(data);
};
/*--------------------old version-------------------------------------
let drag_cols = document.getElementsByClassName("place_to_drag");
console.log(drag_cols);
for (let elem of drag_cols) {
    elem.addEventListener('dragover', function() {drag_move(event)})
}
let drag_elements = document.getElementsByClassName("drag_element");
console.log(drag_elements);
for (let elem of drag_elements) {
    console.log(elem);
    elem.draggable = true;
    /*elem.addEventListener("dragstart", (event) => {
      event.target.classList.add('selected');
    });//отслежвание нажатия и начала движения*/
    //elem.addEventListener("dragstart", function() {drag_start(event)} );
    //elem.addEventListener('dragover', function() {drag_move(event)})
    //elem.addEventListener('dragleave', function() {drag_move(event)})
    /*elem.addEventListener('dragover', (event) => {
	  console.log(1);
      event.preventDefault();
      const activeElement = document.querySelector('.selected');
      const currentElement = event.target;
	  console.log(activeElement);
	  console.log(2);
	  console.log(currentElement);
      const isMoveable = activeElement !== currentElement && currentElement.classList.contains('tasks__item');
      console.error(isMoveable)
      if (!isMoveable) {return;}
      const nextElement = (currentElement === activeElement.nextElementSibling) ?
		currentElement.nextElementSibling :
		currentElement;
	document.insertBefore(activeElement, nextElement);
	console.log(123);
    });//отслежвание движения*/
    /*elem.addEventListener('dragend', (event) => {
      event.target.classList.remove('selected');
    });//отслежвание отпускания и окончания движения
}
//const tasksListElement = document.querySelector(`.tasks__list`);
function drag(event) {
console.log(event);
};
function drag_start(event){
  	/*while (elem != null && elem.className.indexOf("moving") == -1) {
        elem = elem.parentElement;
        console.log(elem.className)
    };
    if (elem != null) {elem.classList.add('selected');};*/
    /*if (event.target.className.indexOf("drag_element") != -1){event.target.classList.add('selected');}
};
function drag_move(event) {
    //event.preventDefault();
    const activeElement = document.querySelector('.selected');
    let currentElement = event.target;
	console.log(currentElement);
	while (currentElement != null && currentElement.className.indexOf("place_to_drag") == -1) {
	    currentElement = currentElement.parentElement;
	    //console.log(currentElement != null, currentElement.className.indexOf("col") == -1, currentElement.className, currentElement);
	};

	console.log(1);
	//console.log(currentElement);
	let activeColElement = activeElement;
	while (activeColElement != null && activeColElement.className.indexOf("place_to_drag") == -1) {
	    activeColElement = activeColElement.parentElement;
	    //console.log(activeColElement != null, activeColElement.className.indexOf("col") == -1, activeColElement.className, activeColElement);
	};
	console.log(4);
    const isMoveable = activeColElement !== currentElement;
    //console.info(isMoveable)
    //if (!isMoveable) {return;}
    /*const nextElement = (currentElement === activeElement.nextElementSibling) ?
	urrentElement.nextElementSibling :
	urrentElement;
	document.insertBefore(activeElement, nextElement);*/
	/*console.error(activeElement, currentElement);
	currentElement.appendChild(activeElement);
};


/*let moving_elements = {};
var elems = document.getElementsByClassName('moving');
let elem;
for (var i = 0; i < elems.length; i++) {
    elem = elems[i];
    elem.id = -i - 1
    console.warn(elems);
    //elems[i].onmousedown = function(){mouse_down(elems[i], event)};//function(){};
    //elems[i].onmousemove = mouse_move(elem);//function(){};
    //elem.onmouseup = function(){mouse_up(elem)};//{};
    elems[i].addEventListener("mousedown", function(){mouse_down()});
    elems[i].addEventListener("mousemove", mouse_move);
    elems[i].addEventListener("mouseup", mouse_up);
    console.log(elem.onmousedown);
}

function mouse_down(elem){
    console.log(event)
    console.log(elem);
    let coords = getCoords(elem);
    console.log(elem);
    let shiftX = event.clientX - coords.left;
    let shiftY = event.clientY - coords.top;
    console.info(shiftX + ":" + shiftY)
    elem.style.position = 'absolute';
    console.log(elem[0]);
    //moving_elements[elem] = {shiftX:shiftX,shiftY:shiftY,pressed:true}
    moving_elements[elem.id] = {shiftX:shiftX,shiftY:shiftY,pressed:true}
    console.log(moving_elements)
    return moving_elements
    //document.body.appendChild(elem);
    //moveAt(self);
};

function mouse_move(elem) {
    /*console.log(elem.mousedown);
    console.info(moving_elements);
    console.log(elem in moving_elements);*\/
    console.log(elem.mousedown)
    /*console.log(moving_elements[elem].pressed)
    if (elem in moving_elements && moving_elements[elem].pressed) {
        console.warn(event.pageX + ":" + event.pageY)
        elem.style.left  = event.clientX - moving_elements[elem].shiftX + 'px';
        elem.style.top = event.clientY - moving_elements[elem].shiftY + 'px';
        //console.log(this.style.x + ":" + this.style.y);
        console.log(2);
    }*\/
}

function mouse_up(elem) {
    console.log(-456)
    console.log(elem)
    moving_elements[elem].pressed =false;
    console.info(moving_elements[elem]);
    elem.onmouseup = null;
    document.onmousemove = null;
    document.onmousedown = null;
};

/*let smile = document.getElementById('smilik');
smile.onmousedown = function(e) {
 let coords = getCoords(smile);
let shiftX = e.pageX - coords.left;
let shiftY = e.pageY - coords.top;
smile.style.position = 'absolute';
document.body.appendChild(smile);
moveAt(e);
smile.style.zIndex = 1000; // над другими элементами*/
/*document.onmousemove = function(e) {
 moveAt(e);
};
smile.onmouseup = function() {
document.onmousemove = null;
smile.onmouseup = null;
};
}*\/
//smile.ondragstart = function() { return false; };
function getCoords(elem) {
    let box = elem.getBoundingClientRect();
    return {
        top: box.top,
        left: box.left
    };
}
*/