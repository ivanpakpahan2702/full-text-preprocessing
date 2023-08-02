// Preloader
$(window).load(function () {
  $(".loader").delay(2000).fadeOut("slow");
  $("#overlayer").delay(2000).fadeOut("slow");
});
//Preloader

setInterval(function () {
  if ($("html").hasClass("translated-ltr")) {
    $(".navbar").css("margin-top", "40px");
    $(".offcanvas").css("margin-top", "40px");
  } else {
    $(".navbar").css("margin-top", "0px");
    $(".offcanvas").css("margin-top", "0px");
  }
}, 0);

$("#caseFoldingChecked").change(function () {
  if (this.checked) {
    $("#caseFoldingChecked").attr("caseCheck", "1");
  } else {
    $("#caseFoldingChecked").attr("caseCheck", "0");
  }
});

$("#normalizationChecked").change(function () {
  if (this.checked) {
    $("#slangFile").show();
    $("#normalizationChecked").attr("slangCheck", "1");
  } else {
    $("#slangFile").hide();
    $("#normalizationChecked").attr("slangCheck", "0");
  }
});

$("#stopwordChecked").change(function () {
  if (this.checked) {
    $("#stopwordFile").show();
    $("#stopwordChecked").attr("stopCheck", "1");
  } else {
    $("#stopwordFile").hide();
    $("#stopwordChecked").attr("stopCheck", "0");
  }
});

$("#stemmingChecked").change(function () {
  if (this.checked) {
    $("#stemmingSelect").show();
    $("#stemmingChecked").attr("stemCheck", "1");
  } else {
    $("#stemmingSelect").hide();
    $("#stemmingChecked").attr("stemCheck", "0");
  }
});

function saveFileAs() {
  if ((promptFilename = prompt("Simpan file sebagai", ""))) {
    var textBlob = new Blob([document.getElementById("txtAreaResult").value], {
      type: "text/plain",
    });
    var downloadLink = document.createElement("a");
    downloadLink.download = promptFilename;
    downloadLink.innerHTML = "Download File";
    downloadLink.href = window.URL.createObjectURL(textBlob);
    downloadLink.click();
    delete downloadLink;
    delete textBlob;
  }
}

document.getElementById("save-button").onclick = saveFileAs;

$(function () {
  $("#process").click(function () {
    val = document.getElementById("stemmingSelect").value.length;
    if (
      $("#slangFile").get(0).files.length === 0 &&
      $("#normalizationChecked").attr("slangCheck") == "1"
    ) {
      let SlangtoastLiveExample = document.getElementById("SlangToast");
      let Slangtoast = new bootstrap.Toast(SlangtoastLiveExample);
      Slangtoast.show();

      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "File Slang Word Belum Dimasukkan",
      });
    } else if (
      $("#stopwordFile").get(0).files.length === 0 &&
      $("#stopwordChecked").attr("stopCheck") == "1"
    ) {
      let StoptoastLiveExample = document.getElementById("StopToast");
      let Stoptoast = new bootstrap.Toast(StoptoastLiveExample);
      Stoptoast.show();

      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "File Stop Word Belum Dimasukkan",
      });
    } else if (val <= 0 && $("#stemmingChecked").attr("stemCheck") == "1") {
      let StemtoastLiveExample = document.getElementById("StemToast");
      let Stemtoast = new bootstrap.Toast(StemtoastLiveExample);
      Stemtoast.show();

      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Bahasa Stemming Belum Dipilih",
      });
    } else {
      console.log("files selected.");

      var full_data = new FormData();
      const Data_Array = [
        document.getElementById("slangFile").files[0],
        document.getElementById("stopwordFile").files[0],
      ];

      Data_Array.forEach((value) => {
        full_data.append("files[]", value);
      });

      if (document.getElementById("oneSentenceRad").checked) {
        var radio_sentence = 1;
      } else if (document.getElementById("multiSentenceRad").checked) {
        var radio_sentence = 2;
      }

      full_data.append(
        "case_folding_stat",
        $("#caseFoldingChecked").attr("caseCheck")
      );
      full_data.append(
        "normalization_stat",
        $("#normalizationChecked").attr("slangCheck")
      );
      full_data.append("stop_stat", $("#stopwordChecked").attr("stopCheck"));
      full_data.append("stem_stat", $("#stemmingChecked").attr("stemCheck"));
      full_data.append("stem_val", $("#stemmingSelect").val());
      full_data.append("radio_sentence", radio_sentence);

      full_data.append("main_data", $("#txtAreaInput").val());

      console.log(full_data);

      $.ajax({
        type: "POST",
        dataType: "json",
        url: "/manual/preprocess",
        data: full_data,
        contentType: false,
        cache: false,
        processData: false,
        timeout: 7200000,
        beforeSend: function (xhr, settings) {
          Swal.fire({
            title: "Proses...",
            html: "Harap Menunggu...",
            allowEscapeKey: false,
            allowOutsideClick: false,
            didOpen: () => {
              Swal.showLoading();
            },
          });
          $("#process").prop("disabled", true);
        },
        success: function (data) {
          swal.close();
          Swal.fire({
            title: "Berhasil",
            text: "Proses Telah Selesai",
            icon: "success",
            confirmButtonText: "Tutup",
            footer: "Durasi " + data[6] + " Detik",
          });
          $("#process").prop("disabled", false);
          $("#txtAreaCaseFolding").text(data[0]);
          $("#txtAreaTokenizing").text(data[1]);
          $("#txtAreaSlang").text(data[2]);
          $("#txtAreaStopword").text(data[3]);
          $("#txtAreaStemming").text(data[4]);
          $("#txtAreaResult").text(data[5]);
          $("#duration").text("Durasi " + data[6] + " Detik");
        },
        error: function (x, t, m) {
          if (t === "timeout") {
            $("#process").prop("disabled", false);
            swal.close();
            Swal.fire({
              title: "Kesalahan",
              text: "Periksa koneksi internet",
              icon: "error",
              confirmButtonText: "Tutup",
            });
          } else {
            $("#process").prop("disabled", false);
            swal.close();
            Swal.fire({
              title: "Kesalahan",
              text: "Periksa Format File Yang Diinput",
              icon: "error",
              footer:
                "Download Format <a href='/static/formats/format_file.rar'>&nbsp;Disini</a>",
              confirmButtonText: "Tutup",
            });
          }
        },
      });
    }
    window.setTimeout(function () {
      $(".alert")
        .fadeTo(500, 0)
        .slideUp(500, function () {
          $(this).remove();
        });
    }, 4000);
  });
});
