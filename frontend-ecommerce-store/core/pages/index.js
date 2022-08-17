import { makeStyles } from "@material-ui/core/styles"
import theme from "../src/theme"

const useStyles = makeStyles((theme) => ({

}))

function Home({posts}) {
  const classes = useStyles()

  return (
    <div>
      <h1>Primeira pagina</h1>
      {posts.map((post) => (
        <p>{post.title}</p>
      ))}
      {console.log(posts)}
    </div>
  )
}

export async function getStaticProps() {
  const res = await fetch("http://localhost:8000/api/v1/")
  const posts = await res.json()

  return {
    props: {
      posts
    }
  }
}

export default Home