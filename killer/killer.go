components {
  id: "script"
  component: "/killer/killer.script"
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"run\"\n"
  "material: \"/materials/pixel_sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/killer/killer.tilesource\"\n"
  "}\n"
  ""
  position {
    x: 3.0
    y: 63.0
  }
}
