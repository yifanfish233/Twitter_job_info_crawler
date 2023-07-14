const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const topTweets = document.getElementById("top-tweets");

searchForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const query = searchInput.value;
    const response = await fetch("/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
    });
    const data = await response.json();
    topTweets.innerHTML = "";
    data.tweets.forEach((tweet) => {
        const li = document.createElement("li");
        li.innerText = tweet;
        topTweets.appendChild(li);
    });
});
