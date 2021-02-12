
$('.tooltiptext').hide();
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url('+e.target.result +')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imageUpload").change(function() {
    readURL(this);
});



function readURL(event){

         var getImagePath = URL.createObjectURL(event.target.files[0]);
         $('#battlefield').css('background-image', 'url(' + getImagePath + ')');
         $('#battlefield').css('height','500px' );
        }

function capitalize(s)
{
    return s[0].toUpperCase() + s.slice(1);
}

document.getElementById("customButton").addEventListener("click", function(){
  document.getElementById("getval").click();  // trigger the click of actual file upload button
});

document.getElementById("getval").addEventListener("change", function(){
  var fullPath = document.getElementById('getval').value;
  var fileName = fullPath.split(/(\\|\/)/g).pop();  // fetch the file name
  document.getElementById("fileName").innerHTML = fileName;  // display the file name
}, false);



$('#customButton').on('mouseover',function(){
    $('.tooltiptext').show();
    
});
$('#customButton').on('mouseleave',function(){
    $('.tooltiptext').hide();
    
});