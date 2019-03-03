//
//  STOMACHViewController.swift
//  MedicPlus
//
//  Created by Alexandra Gafencu on 2019-03-03.
//  Copyright © 2019 Alexandra Gafencu. All rights reserved.
//

import UIKit

class STOMACHViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var label: UILabel!
    
    @IBAction func stepper(_ sender: UIStepper) {
        var number=0
        number=Int(sender.value)
        label.text=String(number)
    }
    
    
    @IBAction func checkBoxTapped(_ sender: UIButton){
        if sender.isSelected{
            sender.isSelected=false
        }else{
            sender.isSelected=true
        }
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
