//
//  Model.swift
//  ChatApp
//
//  Created by Isha Chirimar on 6/13/18.
//  Copyright © 2018 Isha Chirimar. All rights reserved.
//

import Foundation

class Model {
    
    func makeGetCall(){
        let endPoint : String = "http://10.191.62.200:5000/getMessages"
        guard let url = URL(string: endPoint) else {
            print("Error")
            return
        }
        let urlRequest = URLRequest(url: url)
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        
        let task = session.dataTask(with: urlRequest) {
            (data, response, error) in
            guard error == nil else {
                print("error")
                print(error)
                return
            }
            
            guard let responseData = data else {
                print("error: did not get data")
                return
            }
            // parse the result as JSON, since that's what the API provides
            do {
                guard let message = try JSONSerialization.jsonObject(with: responseData, options: [])
                    as? [String: Any] else {
                        print("error trying to convert data to JSON")
                        return
                }
                
                print(message.description)
                
            } catch  {
                print("error trying to convert data to JSON")
                return
            }
        }
        task.resume()
        
    }
    func makePostCall() {
        let endpoint: String = "http://10.191.62.200:5000/message"
        guard let url = URL(string: endpoint) else {
            print("Error: cannot create URL")
            return
        }
        var urlRequest = URLRequest(url: url)
        urlRequest.httpMethod = "POST"
        let message: [String : Any] = ["text" : "hello", "123" : "hi there!"]
        let json: Data
        do {
            json = try JSONSerialization.data(withJSONObject: message, options: [])
            print(json.description)
            urlRequest.httpBody = json
        } catch {
            print("Error: cannot create JSON")
            return
        }
        
        let session = URLSession.shared
        
        let task = session.dataTask(with: urlRequest) {
            (data, response, error) in
            guard error == nil else {
                print("error calling POST")
                print(error!)
                return
            }
            guard let responseData = data else {
                print("Error: did not receive data")
                return
            }
            
           
        }
        task.resume()
    }
}
