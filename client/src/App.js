import { Route, Routes } from "react-router-dom";
import MainPage from "./pages/MainPage";
import LoginPage from "./pages/LoginPage";
import MyPage from "./pages/MyPage";
import SignupPage from "./pages/SignupPage";
import DetailPage from "./pages/DetailPage";
import CreatePage from "./pages/CreatePage";
import Header from "./components/Header";
import Footer from "./components/Footer";
import './App.css';

function App() {


  // const mydivRef = useRef(null);

    // const styles = {S
    //   outer: {
          
    //       height: 300, 
    //       width: 300, 
    //       overflow: 'auto', 
    //       position: 'relative'
    //   }, 
    //   inner:{
    //       width: '100%', 
    //       height: 650, 
    //       background: 'linear-gradient(white, black)'
    //   }
    // };
    
    // const scrollTop = () => mydivRef.current.scrollTop = 0;
    // const scrollBottom = () => mydivRef.current.scrollTop = mydivRef.current.scrollHeight - mydivRef.current.clientHeight;

  return (
    <>
    {/* <div style={styles.outer} ref={mydivRef}>
                <div style={styles.inner}></div>
            </div>
            <div style={{marginTop: 20}}>
                <button onClick={scrollTop}>맨 위로 이동</button>
                <button onClick={scrollBottom}>맨 아래로 이동</button>
            </div> */}
    
      <Header/>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/mypage" element={<MyPage/>}/>
        <Route path="/login/signup" element={<SignupPage/>}/>

        


        {/* /detail/:id 형식 참고해주세요 */}
        <Route path="/detail/:id" element={<DetailPage/>}/>
        <Route path="/create" element={<CreatePage/>}/>
      </Routes>
      <Footer/>
    </>
    
  );
}

export default App;