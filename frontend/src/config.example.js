// Firebase
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "YourAPIKey",
  authDomain: "youDomain.firebaseapp.com",
  projectId: "yourProjectID",
  storageBucket: "yourDomain.appspot.com",
  messagingSenderId: "YourMessagingSenderId",
  appId: "yourAppId"
};

initializeApp(firebaseConfig)

const auth = getAuth()

export { auth }