  
	// -[Prediksi Model]---------------------------
  
	// Fungsi untuk memanggil API ketika tombol prediksi ditekan
	$("#prediksi_submit").click(function(e) {
	  e.preventDefault();
  
	  // Get File Gambar yg telah diupload pengguna
	  var file_data = $('#input_gambar').prop('files')[0];
	  var pics_data = new FormData();
	  pics_data.append('file', file_data);
  
	  // Panggil API dengan timeout 1 detik (1000 ms)
	  setTimeout(function() {
		try {
		  $.ajax({
			url: "/api/deteksi",
			type: "POST",
			data: pics_data,
			processData: false,
			contentType: false,
			success: function(res) {
			  // Ambil hasil prediksi dan path gambar yang diprediksi dari API
			  var res_data_prediksi = res['prediksi'];
			  var res_gambar_prediksi = res['prediksi_submit'];
  
			  // Tampilkan hasil prediksi ke halaman web
			  generate_prediksi(res_data_prediksi, res_gambar_prediksi);
			},
			error: function(xhr, status, error) {
			  console.log(xhr.responseText);
			}
		  });
		} catch (e) {
		  // Jika gagal memanggil API, tampilkan error di console
		  console.log("Gagal !");
		  console.log(e);
		}
	  }, 1000);
	});
  
	// Fungsi untuk menampilkan hasil prediksi model
	function generate_prediksi(data_prediksi, image_prediksi) {
	  var str = "";
  
	  if (image_prediksi == "(none)") {
		str += "<h4><b>Hasil Prediksi</b></h4>";
		str += "<br>";
		str += "<p>Silahkan masukkan file gambar (.jpg)</p>";
	  } else {
		str += "<h4><b>Hasil Prediksi</b></h4>";
		str += "<img src='" + image_prediksi + "' width='150'></img>";
    str += "<br><br>";
		str += "<p>ini klasifikasi kanker kulit :<b> " + data_prediksi + "</b></p>";
	  }
	  $("#hasil_prediksi").html(str);
	}
  
  