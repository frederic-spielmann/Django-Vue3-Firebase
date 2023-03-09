import { defineStore } from "pinia"
import {
    createUserWithEmailAndPassword,
    onAuthStateChanged,
    signInWithEmailAndPassword,
    signOut,
    getIdToken,
    sendPasswordResetEmail,
    confirmPasswordReset,
    updateProfile,
    updateEmail,
    updatePassword,
    deleteUser
} from "firebase/auth"
import { auth } from "@/config"
import router from "@/router"
import {cfetch} from "../utils/cfetch";

export const useUsersStore = defineStore("userStore", {
    state: () => ({
        userData: null,
        loadingUser: false,
        loadingSession: false,
    }),
    actions: {
        // + create in postgres with email + UserID
        async register(email, password, displayName) {
            this.loadingUser = true
            try {
                const { user } = await createUserWithEmailAndPassword(
                    auth,
                    email,
                    password
                )
                await updateProfile(auth.currentUser, {
                    displayName: displayName, photoURL: ''
                })
                this.userData = { email: user.email, uid: user.uid }
                router.push("/")
            } catch (error) {
                switch(error.code) {
                  case 'auth/email-already-in-use':
                    alert("Email already in use")
                    break
                  case 'auth/invalid-email':
                    alert("Invalid email")
                    break
                  case 'auth/operation-not-allowed':
                    alert("Operation not allowed")
                    break
                  case 'auth/weak-password':
                    alert("Weak password")
                    break
                  default:
                    alert("Something went wrong")
                }
            } finally {
                this.loadingUser = false
            }
        },
        async login(email, password) {
            this.loadingUser = true
            try {
                const { user } = await signInWithEmailAndPassword(
                    auth,
                    email,
                    password
                )
                this.userData = { email: user.email, uid: user.uid }
                router.push("/")
            } catch (error) {
                switch(error.code) {
                  case 'auth/user-not-found':
                    alert("User not found")
                    break
                  case 'auth/wrong-password':
                    alert("Wrong password")
                    break
                  default:
                    alert("Something went wrong")
                }
            } finally {
                this.loadingUser = false
            }
        },

        async logout() {
            try {
                await signOut(auth)
                this.userData = null
                router.push("/login")
            } catch (error) {
                console.log(error)
            }
        },

        async resetPassword(email) {
            try {
                const actionCodeSettings = { url: 'http://localhost:5173/?email=' + email }
                await sendPasswordResetEmail(auth, email, actionCodeSettings)
            .then(x => {x})
                alert("email successfully sent")
            } catch (error) {
                switch(error.code) {
                  case 'auth/user-not-found':
                    alert("User not found")
                    break
                  default:
                    alert("Something went wrong")
                }
            }
        },

        async confirmPasswordReset(oobCode, newPassword) {
            try {
                await confirmPasswordReset(auth, oobCode, newPassword)
            .then(x => {x})
                alert("password has been successfully changed")
                router.push("/login")
            } catch (error) {
                switch(error.code) {
                  default:
                    alert("Something went wrong")
                }
            }
        },

        currentUser() {
            return new Promise((resolve, reject) => {
                const unsubscribe = onAuthStateChanged(
                    auth,
                    (user) => {
                        if (user) {
                            this.userData = {
                                email: user.email,
                                displayName: user.displayName,
                                photoURL: user.photoURL,
                                uid: user.uid,
                            }
                        } else {
                            this.userData = null
                        }
                        resolve(user)
                    },
                    (e) => reject(e)
                )
                unsubscribe()
            })
        },

        async updateUser(displayName, photoURL, email, password) {
            if(email && this.userData.email !== email) {
                await updateEmail(auth.currentUser, email).then(() => {
                    alert("email updated")
                }).catch((error) => {
                    alert(error)
                })
            }

            if(password && this.userData.password !== password) {
                await updatePassword(auth.currentUser, password).then(() => {
                  alert("password updated")
                }).catch((error) => {
                  alert(error)
                })
            }

            if((displayName && this.userData.displayName !== displayName) || (photoURL && this.userData.photoURL !== photoURL)){
                await updateProfile(auth.currentUser, {
                    displayName: displayName, photoURL: photoURL
                }).then(() => {
                    alert("Profile Updated!")
                }).catch((error) => {
                    alert(error)
                })
            }

        },

        async deleteUser(){
            //this.do('delete', 'user')
            await cfetch.delete('user')
            deleteUser(auth.currentUser)
              .then(() => {
              alert("Account has been deleted")
              this.userData = null
              router.push("/login")
            }).catch((error) => {
              alert(error)
                if(error === "CREDENTIAL_TOO_OLD_LOGIN_AGAIN") {
                    this.logout()
                }
            })
        },
    },
})
