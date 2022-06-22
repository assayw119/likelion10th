import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [posts, setposts] = useState([]);

  const getData = async () => {
    const res = await axios('http://127.0.0.1:8000/');
    const data = res.data;
    setposts(data);
};

  useEffect(() => {
    try {
      getData();
    } catch (e) {
      console.log(e);
    }
}, []);
  return (
    <div>
      {/* map 함수로 array 데이터 가져옴 */}
      {posts.map((item) => {
        return (
        <div key={item.id}>
          <h1>{item.title}</h1>
          <span>{item.content}</span>
        </div>
        );
      })}
    </div>
  );
  

}

export default App;

