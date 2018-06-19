//
//  ViewController.swift
//  ChatApp
//
//  Created by Isha Chirimar on 6/13/18.
//  Copyright © 2018 Isha Chirimar. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    @IBOutlet weak var button: UIButton!
    @IBAction func buttonClicked(_ sender: UIButton) {
        let session = Model()
        //session.makeGetCall()
        session.makePostCall()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

