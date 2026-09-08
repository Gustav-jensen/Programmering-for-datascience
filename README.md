# Programmering-for-datascience
# Første opgave beregn gennemsnittet af inflammation pr. dag
inflammation <- read.csv(
  file = "data/inflammation-01.csv",
  header = FALSE
)

dat <- read.csv(file = "data/inflammation-01.csv", header = FALSE)

average_inflamation <- colMeans(dat)

plot(
  average_inflamation,
  type = "l",
  xlab = "Dag",
  ylab = "Gennemsnitlig inflammation",
  main = "Gennemsnitlig inflammation pr. dag"
)
