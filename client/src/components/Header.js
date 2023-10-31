import { Link, useNavigate, useLocation  } from "react-router-dom";
import styles from "./Header.module.css";
import { RiAuctionFill } from "react-icons/ri";
import { useEffect, useState } from "react";
import {
  AiOutlineSearch,
  AiOutlineShoppingCart,
  AiOutlineUser,
} from "react-icons/ai";

function Header() {
  const [keyword, setKeyword] = useState("");
  const isLogin = localStorage.getItem('token'); // 토큰이 존재하는지 확인

  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    // 로그아웃 시 localStorage의 토큰 제거
    localStorage.removeItem('token');
    localStorage.removeItem('userId');
    navigate("/");
  };
  const handlerMyPage = () => {
    if (isLogin) {
      navigate('/mypage');
    } else {
      const confirmLogin = window.confirm('로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?');
      if (confirmLogin) {
        navigate('/login');
      }
    }
  };

  const handlerAuction = () => {
    if (isLogin) {
      navigate('/create');
    } else {
      const confirmLogin = window.confirm('로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?');
      if (confirmLogin) {
        navigate('/login');
      }
    }
  };
  const handleSubmit = (e) => {
    e.preventDefault(); // onSubmit 시 새로고침 기본동작 방지
    // 유효성 검사 추가할 것.
    console.log("here")
    setKeyword(''); // Reset keyword to clear the search input
    navigate('/', { state: { query: keyword } });
    
  };
  const handleKeyword = (event) => {
    setKeyword(event.target.value);
    console.log(`키워드상태관리: ${event.target.value}`);
  };

  return (
    <div className={styles.container}>
      <div className={styles.first}>
        <div className={styles.first1}>
          <div className={styles.first2}>
          {
            isLogin  ? (<button onClick={handleLogout}>로그아웃</button>) : 
            (<button><Link to='/login'>로그인/회원가입</Link></button>)
          }

          </div>
        </div>
      </div>
      <div className={styles.second}>
        <div className={styles.second1}>
          <Link className={styles.title_image} to="/">
            <RiAuctionFill></RiAuctionFill>
            <span className={styles.ssg}>쓱</span>Bay
          </Link>
          <form onSubmit={handleSubmit} className={styles.searchBar}>
            <input
              type="text"
              className={styles.searchInput}
              placeholder="검색"
              onChange={handleKeyword}
              value={keyword}
            />
            <button className={styles.searchButton}>
              <AiOutlineSearch></AiOutlineSearch>
            </button>
          </form>
          <div className={styles.tabs}></div>
            <button className={styles.tabLink} onClick={handlerAuction}>
            <AiOutlineShoppingCart/>경매
            </button>
            <div className={styles.line}></div>
            <button className={styles.tabLink} onClick={handlerMyPage}>
            <AiOutlineUser/>마이페이지
            </button>
            
          
        </div>
      </div>
    </div>
  );
}

export default Header;