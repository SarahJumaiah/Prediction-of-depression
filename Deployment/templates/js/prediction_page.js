// Retrieve prediction result from local storage
var predictionResult = localStorage.getItem("overallDepressionStatus");
if (predictionResult) {
  var prediction_result_div = document.querySelector(".prediction_result");
  if (predictionResult) {
    prediction_result_div.innerHTML =
      predictionResult;
  }
}