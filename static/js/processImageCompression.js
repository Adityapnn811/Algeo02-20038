function process_image_compression() {
  
  var x = document.getElementById("inputPercentage").value;

  if (x == '') {
    swal("You have to give value to Image Compression Ratio!");
    return;
  }

  const file = document.querySelector("#upload").files[0];

  if (!file) { 
    swal("You have to give image!");
    return;
  }

  swal("Please Wait~");

  var files = document.getElementById("upload").files
  var formData = new FormData();
  var endpoint = '/api/v1/convert_image';
  formData.append('image', files[0]);
  formData.append('inputPercentage', x);

  $.ajax({
    type: 'POST',
    url: endpoint,
    data: formData,
    contentType: false,
    cache: false,
    processData: false,
    success: function(data) {
      getConvertedFiles(data.filename, data.waktu);
      showUpBefore(file);
      showUpTime(x);
    }
  });

  function getConvertedFiles(filename, waktu) {
    document.querySelector("#output").src = "static/image/"+ filename;
    document.getElementById("outputTime").innerHTML = waktu + ' seconds';
  }

  function showUpBefore(file){
    const reader = new FileReader();

    reader.readAsDataURL(file);
  
    reader.onload = function (event) {
      const imgElement = document.createElement("img");
      imgElement.src = event.target.result;
      document.querySelector("#input").src = event.target.result;
    };
  }
  
  function showUpTime(x){
    document.getElementById("outputPercentage").innerHTML = x;
  }
}