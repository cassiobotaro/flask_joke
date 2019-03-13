workflow "lint" {
  on = "push"
  resolves = ["lgeiger/black-action@master"]
}

action "lgeiger/black-action@master" {
  uses = "lgeiger/black-action@master"
}
