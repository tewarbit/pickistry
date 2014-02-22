myFunction = function() {
  
  var params = "";
  var emails = document.getElementsByName("email");
  for (var i = emails.length - 1; i >= 0; i--) {
    params = params + "Email=" + emails[i].value + "&";
  };
  params = params.substring(0, params.length - 1);

  var responseField = document.getElementById("response");

  var img = document.createElement("img");
  img.src = "images/loading.gif";

  var xhr = createXHR();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      //responseField.value = xhr.responseText;
      showPanel(xhr.responseText)
    }
  }

  var fieldNameElement = document.getElementById("putresponse");
  clearResponseDiv();
  fieldNameElement.appendChild(img);
  
  // xhr.open('POST', '/initiate?Email=btewari@gmail.com', true);
  xhr.open('POST', '/initiate?' + params, true);
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhr.send();
}

function showPanel(fieldName) {
  var fieldNameElement = document.getElementById("putresponse");
  clearResponseDiv();
  fieldNameElement.appendChild(fieldNameElement.ownerDocument.createTextNode(fieldName));
}

function clearResponseDiv() {
  var fieldNameElement =  document.getElementById("putresponse");
  while(fieldNameElement.childNodes.length >= 1) {
    fieldNameElement.removeChild(fieldNameElement.firstChild);
  }
}