import firebase from "firebase";
import "firebase/auth";
import "firebase/firestore";
// import auth from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDaiJ_xr4853ITPKcAM3DPRkZ1IxDMpsfg",
  authDomain: "job-application-manager-a297d.firebaseapp.com",
  databaseURL:
    "https://job-application-manager-a297d-default-rtdb.firebaseio.com",
  projectId: "job-application-manager-a297d",
  storageBucket: "job-application-manager-a297d.appspot.com",
  messagingSenderId: "513298061745",
  appId: "1:513298061745:web:b2aaf1c8ee797c8b5ec590",
  measurementId: "G-6ZQFFCS9ZC",
};

firebase.initializeApp(config);

const provider = new firebase.auth.GoogleAuthProvider();
const auth = auth();
const firestore = firebase.firestore();

const signInWithGoogle = () => {
  auth.signInWithPopup(provider);
};