function calc() {
  var marks = document.getElementById("marks").value;
  if (marks < 40) {
    document.write("Fail!");
  } else if (marks >= 40 && marks <= 60) {
    document.write("Good!");
  } else if (marks > 60) {
    document.write("Vary Good!");
  } else if (marks > 90) {
    document.write("Excellent!");
  }
}
var j = 0;
do {
  document.write("J is ->" + j + "<br>");
  j++;
} while (j <= 10);
var userName = "ADII22032002";
for (n in userName) {
  document.write(n + "  ");
}
document.write("<br>");