use raylib::{prelude::*};
fn main() {
    let (mut rl, thread) = raylib::init()
        .size(640, 480)
        .title("asciier")
        .build();

    let shapes = [
        " ", //0
        "/", //1
        "|", //2
        "\\",//3
        "-", //4
        "_", //5
        ".", //6
        ",", //7
        ":", //8
        ";", //9
        "L", //A
        "I", //B
        "O", //C
        "T", //D
        "X", //E
        "x", //F
    ];
    let pyshapes = [
        " ", //0
        "/", //1
        "|", //2
        "\\\\",//3
        "-", //4
        "_", //5
        ".", //6
        ",", //7
        ":", //8
        ";", //9
        "L", //A
        "I", //B
        "O", //C
        "T", //D
        "X", //E
        "x", //F
    ];
    let mut frames: Vec<[[usize; 30]; 20]> = vec![
        [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    ];

    let template = vec![[
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]];

    let mut current = 0;
    let mut brush = 1;
    let mut isgrid = true;
    let mut play = false;

    let font = rl.load_font_ex(&thread,"font.ttf", 32, None).unwrap();
    let smont = rl.load_font_ex(&thread,"font.ttf", 16, None).unwrap();

    while !rl.window_should_close() {
        let mut d = rl.begin_drawing(&thread);

        d.clear_background(Color::BLACK);
        if d.is_key_down(KeyboardKey::KEY_M){
            d.draw_text_ex(&font, "asciier\nsimple ascii animation maker\nmanual\nup/down to go through brushes\nleft/right to go through frames\ng to toggle grid\ne to export\ns to save\np to play\nc to copy frame", Vector2::new(0.0,0.0),32.0,1.0,Color::WHITE);

        } else{
            //d.draw_text("Hello, world!", 12, 12, 20, Color::WHITE);
            d.draw_text_ex(&font, "asciier", Vector2::new(0.0,0.0),32.0,1.0,Color::WHITE);
            d.draw_text_ex(&smont, &(" frames: ".to_owned()+&frames.len().to_string()), Vector2::new(0.0,40.0),16.0,1.0,Color::WHITE);
            d.draw_text_ex(&smont, &(" current: ".to_owned()+&(current+1).to_string()), Vector2::new(0.0,50.0),16.0,1.0,Color::WHITE);
            d.draw_text_ex(&smont, &(" brush: ".to_owned()+&shapes[brush]), Vector2::new(0.0,60.0),16.0,1.0,Color::WHITE);
            for x in 0..30{
                for y in 0..20{
                    if isgrid{
                        d.draw_rectangle_lines(120+ 16*x,24+ 22*y,16,24,Color::DARKGRAY);
                    }
                    d.draw_text_ex(&font, shapes[frames[current][y as usize][x as usize]], Vector2::new(120.0+ 16.0*(x as f32),20.0+ 22.0*(y as f32)),32.0,1.0,Color::WHITE);
                    if d.get_mouse_x() > 120+ 16*x && d.get_mouse_x() < 136+ 16*x && d.get_mouse_y() > 24+ 22*y && d.get_mouse_y() < 46+ 22*y && d.is_mouse_button_down(MouseButton::MOUSE_BUTTON_LEFT ) {
                        frames[current][y as usize][x as usize] = brush;
                    }
                }
            }
            //d.draw_fps(0, 500);
            if d.is_key_pressed(KeyboardKey::KEY_P){
                play = !play;
                if play{
                    d.set_target_fps(10);
                }else{
                    d.set_target_fps(60);
                }
            }
            if play{
                current+=1;
                if current == frames.len(){
                    current=0;
                }
                //std::thread::sleep(std::time::Duration::from_secs(0.1 as u64));
            }else{
                
                if d.is_key_pressed(KeyboardKey::KEY_G){
                    isgrid = !isgrid;
                }
                if d.is_key_pressed(KeyboardKey::KEY_RIGHT){
                    current+=1;
                    if current == frames.len(){
                        frames.append(&mut template.clone());
                    }
                }
                if d.is_key_pressed(KeyboardKey::KEY_C){
                    frames.push(frames[current]);
                    current+=1;
                }
                if d.is_key_pressed(KeyboardKey::KEY_LEFT){
                    if current>0{
                        current-=1;
                    }
                }
                if d.is_key_pressed(KeyboardKey::KEY_DOWN){
                    brush+=1;
                    if brush == shapes.len(){
                        brush=0;
                    }
                }
                if d.is_key_pressed(KeyboardKey::KEY_UP){

                    if brush == 0{
                        brush=shapes.len();
                    }

                    brush-=1;
                    
                }
                if d.is_key_pressed(KeyboardKey::KEY_D){
                    if frames.len() > 1{
                        frames.remove(current);
                        if current >0{
                            current-=1;
                        }
                    }
                }if d.is_key_pressed(KeyboardKey::KEY_S){
                    sav(&frames);
                }if d.is_key_pressed(KeyboardKey::KEY_L){
                    frames = ld(&template);
                }if d.is_key_pressed(KeyboardKey::KEY_E){
                    pyexport(&frames, pyshapes);
                }
            }
        }
    }
}


fn sav(map: &Vec<[[usize; 30]; 20]>){
    let byts: Vec<u8> = map.iter().flatten().flatten().map(|&x| x as u8).collect::<Vec<_>>().chunks(2).map(|x| (x[0] << 4) | x[1]).collect();
    std::fs::write("anim.cas", byts).unwrap();
}

fn ld(template:&Vec<[[usize; 30]; 20]>) -> Vec<[[usize; 30]; 20]>{
    let byts = std::fs::read("anim.cas").unwrap();
    let mut result: Vec<[[usize; 30]; 20]> = vec![];
    let size= byts.len() * 2;
    let fnum = (size as f32/600.0).floor() as i32;
    println!("{size},{fnum}: {:?}", byts);
    let mut truebytes: Vec<u8> = vec![];
    for byte in byts.iter().enumerate(){
        truebytes.push((byts[byte.0] as f32/16.0).floor() as u8);
        truebytes.push(byts[byte.0]%16);
    }
    println!("{:?}", truebytes);
    for frame in 0..fnum{
        let mut abwebwe = 0;
        let mut bingus = template[0];
        for x in 0..20{
            for y in 0..30{
                bingus[x][y] = truebytes[(abwebwe+(frame*600)) as usize] as usize;
                abwebwe+=1;
            }
        }
        result.push(bingus);
    }
    
    result
}


fn pyexport(frames:&Vec<[[usize; 30]; 20]>, shapes:[&str; 16] ){
    let header = "frames = [\"\"\"";
    let inbetween = "\"\"\",\"\"\"";
    let framend = "\"\"\"]\n";
    let ending = "import time\n\nwhile True:\n	for i in range(len(frames)):\n		for q in range(5):\n			print(frames[i])\n		time.sleep(0.1)";
    let mut fl = header;
    let mut add: String;

    
    for i in 0..frames.len(){
        if i != 0{
            add = fl.to_owned() + inbetween;
            fl = &add;
        }

        for x in 0..20{
            for y in 0..30{
                //omfg im so done w this shit
                add = fl.to_owned() + shapes[frames[i][x][y]];
                fl = &add;
            }
            add = fl.to_owned() + "\n";
            fl = &add;
            
        }
    }
    add = fl.to_owned() + framend;
    fl = &add;
    add = fl.to_owned() + ending;
    fl = &add;
    
    std::fs::write("anim.py",fl).unwrap();
}

