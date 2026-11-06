// Adresa backenda (zamijeni svojom, BEZ / na kraju)
const API_URL = "https://miniblog-vdadic-api.onrender.com";


// GET - dohvati sve objave i prikaži ih
async function loadPosts() {
  const response = await fetch(API_URL + "/posts");
  const posts = await response.json();

  let html = "";

  for (const post of posts) {
    html += `
      <div class="post">
        <h2>${post.title}</h2>
        <p class="date">${post.date}</p>
        <p>${post.content}</p>
        <button onclick="deletePost(${post.id})">Obriši</button>
      </div>
    `;
  }

  document.getElementById("posts").innerHTML = html;
}


// POST - pošalji novu objavu
async function addPost() {
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;

  await fetch(API_URL + "/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: title, content: content })
  });

  document.getElementById("title").value = "";
  document.getElementById("content").value = "";

  loadPosts();
}


// DELETE - obriši objavu
async function deletePost(id) {
  await fetch(API_URL + "/posts/" + id, { method: "DELETE" });

  loadPosts();
}


// Učitaj objave odmah po otvaranju stranice
loadPosts();