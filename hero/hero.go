components {
  id: "deathfx"
  component: "/particles/death.particlefx"
  position {
    y: 40.0
    z: 0.1
  }
}
components {
  id: "script"
  component: "/hero/hero.script"
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"run\"\n"
  "material: \"/materials/pixel_sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/hero/Guy.tilesource\"\n"
  "}\n"
  ""
  position {
    x: 17.0
    y: 63.0
  }
}
