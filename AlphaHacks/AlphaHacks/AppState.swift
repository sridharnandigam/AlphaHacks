//
//  Postman.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct CompanyStats : Codable {
    var description: String
    var rating: Float
    var articles: [Article]
}

struct Article : Codable {
    var article_title: String
    var description: String
    var link: String
    var image_link: String
}

struct POST_image_RESPONSE: Codable {
    var companies: [String]
}

class AppState : ObservableObject {
    @Published var companies = ["Test Company 1", "Test Company 2", "Test Company 3"]
    @Published var competitors = ["Test Company 4", "Test Company 5", "Test Company 6"]
    @Published var selectedCompany = "Test Company 1"
    @Published var company_details = CompanyStats(
        description: "Test Description Test Description Test Description Test Description Test Description Test Description Test Description Test Description Test Description Test Description ",
        rating: 420.69,
        articles: [
            Article(article_title: "Article Title 1 An Article Title about the Article", description: "Article Description 1", link: "https://google.com", image_link: "https://lp-cms-production.imgix.net/2021-01/Nasa%201.jpeg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850"),
            Article(article_title: "Article Title 2 An Article Title about the Article", description: "Article Description 2", link: "https://apple.com", image_link: "https://lp-cms-production.imgix.net/2021-01/Nasa%201.jpeg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850"),
        ]
    )
    @Published var imageDict = [String: UIImage]()
    
    func POST_image(image: UIImage) {
        DispatchQueue.global().async {
            let boundary = "Boundary-\(UUID().uuidString)"

            var request = URLRequest(url: URL(string: "https://pranay's server")!)
            request.httpMethod = "POST"
            request.setValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
            
            let httpBody = NSMutableData()
            
            let imageData = image.pngData()!

            httpBody.append(convertFileData(fieldName: "image_field",
                                            fileName: "imagename.png",
                                            mimeType: "image/png",
                                            fileData: imageData,
                                            using: boundary))

            httpBody.appendString("--\(boundary)--")

            request.httpBody = httpBody as Data
            
            URLSession.shared.dataTask(with: request) { data, response, error in
                guard let data = data else { return }
                let response_data = try? JSONDecoder().decode(POST_image_RESPONSE.self, from: data)
                if let json_data = response_data {
                    DispatchQueue.main.async {
                        self.companies = json_data.companies
                    }
                }
            }.resume()
        }
    }
    
    func GET_competitors(company: String) {
        let url = URL(string: "https://pranay's server/competitors?company=\(company)")!
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data else { return }
            let response_data = try? JSONDecoder().decode(POST_image_RESPONSE.self, from: data)
            if let json_data = response_data {
                DispatchQueue.main.async {
                    self.competitors = json_data.companies
                }
            }
        }
        task.resume()
    }
    
    func GET_stats(company: String) {
        let url = URL(string: "https://pranay's server/stats?company=\(company)")!
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data else { return }
            let response_data = try? JSONDecoder().decode(CompanyStats.self, from: data)
            if let json_data = response_data {
                DispatchQueue.main.async {
                    self.company_details = json_data
                }
            }
        }
        task.resume()
    }
}

func convertFormField(named name: String, value: String, using boundary: String) -> String {
  var fieldString = "--\(boundary)\r\n"
  fieldString += "Content-Disposition: form-data; name=\"\(name)\"\r\n"
  fieldString += "\r\n"
  fieldString += "\(value)\r\n"

  return fieldString
}

func convertFileData(fieldName: String, fileName: String, mimeType: String, fileData: Data, using boundary: String) -> Data {
  let data = NSMutableData()

  data.appendString("--\(boundary)\r\n")
  data.appendString("Content-Disposition: form-data; name=\"\(fieldName)\"; filename=\"\(fileName)\"\r\n")
  data.appendString("Content-Type: \(mimeType)\r\n\r\n")
  data.append(fileData)
  data.appendString("\r\n")

  return data as Data
}

extension NSMutableData {
  func appendString(_ string: String) {
    if let data = string.data(using: .utf8) {
      self.append(data)
    }
  }
}
