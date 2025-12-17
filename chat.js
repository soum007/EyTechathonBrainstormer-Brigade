async function send() {
  const input = document.getElementById("input").value;
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({session_id: "demo123", message: input})
  });
  const data = await res.json();
  document.getElementById("chat").innerHTML += `<p><b>You:</b> ${input}</p>`;
  document.getElementById("chat").innerHTML += `<p><b>AI:</b> ${data.response}</p>`;
}
